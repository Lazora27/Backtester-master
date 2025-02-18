import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
