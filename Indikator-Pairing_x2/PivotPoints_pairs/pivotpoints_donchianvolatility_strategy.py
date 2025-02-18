import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'DonchianVolatility': 1.0
        })
    )
