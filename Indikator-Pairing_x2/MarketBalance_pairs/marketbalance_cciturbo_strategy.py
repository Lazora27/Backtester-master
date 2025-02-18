import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketBalance_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketBalance und CCITurbo
    """
    
    params = (
        ('indicators', {
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'MarketBalance': 1.0,
            'CCITurbo': 1.0
        })
    )
