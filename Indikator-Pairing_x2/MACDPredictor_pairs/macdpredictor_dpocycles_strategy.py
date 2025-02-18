import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und DPOCycles
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'DPOCycles': 1.0
        })
    )
