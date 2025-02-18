import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und TrueRange
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'TrueRange': 1.0
        })
    )
