import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und BollingerBands
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'BollingerBands': 1.0
        })
    )
