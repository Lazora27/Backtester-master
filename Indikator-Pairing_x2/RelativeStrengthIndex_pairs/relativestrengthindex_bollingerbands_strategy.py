import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und BollingerBands
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'BollingerBands': 1.0
        })
    )
