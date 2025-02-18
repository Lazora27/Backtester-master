import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und BollingerBands
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'BollingerBands': 1.0
        })
    )
