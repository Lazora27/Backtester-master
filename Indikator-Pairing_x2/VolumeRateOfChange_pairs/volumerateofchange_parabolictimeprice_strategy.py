import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeRateOfChange_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeRateOfChange und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'VolumeRateOfChange': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
