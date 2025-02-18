import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
