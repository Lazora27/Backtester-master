import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und BollingerBands
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'BollingerBands': 1.0
        })
    )
