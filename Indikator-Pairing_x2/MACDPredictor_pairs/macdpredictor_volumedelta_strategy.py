import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_VolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und VolumeDelta
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'VolumeDelta': 1.0
        })
    )
