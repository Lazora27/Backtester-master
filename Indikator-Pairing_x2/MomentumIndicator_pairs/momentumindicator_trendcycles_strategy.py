import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und TrendCycles
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'TrendCycles': 1.0
        })
    )
