import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'LiquidityIndex': 1.0
        })
    )
