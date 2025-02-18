import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und BollingerBands
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'BollingerBands': 1.0
        })
    )
