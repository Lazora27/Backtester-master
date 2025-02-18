import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_VolumeProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und VolumeProfile
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'VolumeProfile': 1.0
        })
    )
