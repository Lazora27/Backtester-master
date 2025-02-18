import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'DonchianVolatility': 1.0
        })
    )
