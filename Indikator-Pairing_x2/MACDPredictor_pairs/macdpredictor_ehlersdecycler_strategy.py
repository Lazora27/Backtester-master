import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'EhlersDecycler': 1.0
        })
    )
