import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'BradleySiderograph': 1.0
        })
    )
