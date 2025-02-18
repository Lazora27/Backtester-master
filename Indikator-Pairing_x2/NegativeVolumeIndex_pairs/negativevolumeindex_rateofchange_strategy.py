import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NegativeVolumeIndex_RateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NegativeVolumeIndex und RateOfChange
    """
    
    params = (
        ('indicators', {
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            },
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            }
        }),
        ('weights', {
            'NegativeVolumeIndex': 1.0,
            'RateOfChange': 1.0
        })
    )
