import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_VolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und VolumeDelta
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'VolumeDelta': 1.0
        })
    )
