import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und BollingerBands
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'BollingerBands': 1.0
        })
    )
