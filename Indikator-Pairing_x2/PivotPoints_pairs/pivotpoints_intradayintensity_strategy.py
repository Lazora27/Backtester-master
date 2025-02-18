import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'IntradayIntensity': 1.0
        })
    )
