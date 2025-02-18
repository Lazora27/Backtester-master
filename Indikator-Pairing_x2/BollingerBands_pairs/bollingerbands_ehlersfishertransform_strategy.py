import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
