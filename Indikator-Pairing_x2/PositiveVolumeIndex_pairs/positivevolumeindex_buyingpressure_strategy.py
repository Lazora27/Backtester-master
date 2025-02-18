import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PositiveVolumeIndex_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PositiveVolumeIndex und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'PositiveVolumeIndex': 1.0,
            'BuyingPressure': 1.0
        })
    )
