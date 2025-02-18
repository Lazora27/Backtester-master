import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
