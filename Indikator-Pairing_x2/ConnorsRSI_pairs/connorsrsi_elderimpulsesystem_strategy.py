import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_ElderImpulseSystem_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und ElderImpulseSystem
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'ElderImpulseSystem': 1.0
        })
    )
