import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_NegativeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und NegativeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'NegativeVolumeIndex': 1.0
        })
    )
