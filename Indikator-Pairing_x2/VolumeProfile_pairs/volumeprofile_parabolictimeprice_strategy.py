import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
