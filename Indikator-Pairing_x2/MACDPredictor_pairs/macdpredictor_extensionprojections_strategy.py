import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'ExtensionProjections': 1.0
        })
    )
