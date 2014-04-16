% if list_title:
    <h3>${list_title}</h3>
% endif

<table class="admin-list">
<thead>
    <tr>
    % for field in view_context.list_fields:
        <td>${field.name}</td>
    % endfor
    </tr>
</thead>
<tbody>
    % for item in list_items:
    <tr>
        % for field in view_context.list_fields:
            <% value = getattr(item, field.attr) %>

            <td>
            % if field.link:
                <a href="${field.link.format(**vars(item))}">
            % endif

            % if value is True:
                &#x2611;
            % elif value is False:
                &#x2612;
            % elif value is not None:
                ${field.filter(value)}
            % endif

            % if field.link:
                </a>
            % endif
            </td>
        % endfor
    </tr>
    % endfor
</tbody>
</table>

