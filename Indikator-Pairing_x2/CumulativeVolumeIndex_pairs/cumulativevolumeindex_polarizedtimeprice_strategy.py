import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeVolumeIndex_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeVolumeIndex und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'CumulativeVolumeIndex': {
                'class': CumulativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeVolumeIndex'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'CumulativeVolumeIndex': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
