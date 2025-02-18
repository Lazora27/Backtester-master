import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
