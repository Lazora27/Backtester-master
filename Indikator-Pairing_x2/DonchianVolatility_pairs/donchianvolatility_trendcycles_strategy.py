import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und TrendCycles
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'TrendCycles': 1.0
        })
    )
