import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_PositiveVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und PositiveVolumeIndex
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'PositiveVolumeIndex': 1.0
        })
    )
