import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
