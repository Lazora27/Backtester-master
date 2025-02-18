import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und CCITurbo
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'CCITurbo': 1.0
        })
    )
