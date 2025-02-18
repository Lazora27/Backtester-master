import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und BarStrength
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'BarStrength': 1.0
        })
    )
