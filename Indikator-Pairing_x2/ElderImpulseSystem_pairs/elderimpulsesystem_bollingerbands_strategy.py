import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und BollingerBands
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'BollingerBands': 1.0
        })
    )
