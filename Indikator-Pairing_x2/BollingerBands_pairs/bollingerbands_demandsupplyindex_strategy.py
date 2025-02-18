import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
