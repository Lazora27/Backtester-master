import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und BollingerBands
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'BollingerBands': 1.0
        })
    )
