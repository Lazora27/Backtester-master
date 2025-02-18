import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
