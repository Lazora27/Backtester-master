import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
