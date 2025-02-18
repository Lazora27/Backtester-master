import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und GannAngles
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'GannAngles': 1.0
        })
    )
