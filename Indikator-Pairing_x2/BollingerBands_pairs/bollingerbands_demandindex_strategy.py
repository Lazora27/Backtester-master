import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und DemandIndex
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'DemandIndex': 1.0
        })
    )
