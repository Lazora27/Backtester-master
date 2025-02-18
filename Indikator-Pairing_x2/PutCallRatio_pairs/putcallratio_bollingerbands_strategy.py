import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und BollingerBands
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'BollingerBands': 1.0
        })
    )
