import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'DeltaProfile': 1.0
        })
    )
