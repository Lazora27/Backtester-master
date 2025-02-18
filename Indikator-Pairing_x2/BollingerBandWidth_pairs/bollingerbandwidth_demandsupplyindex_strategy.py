import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandWidth_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandWidth und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'BollingerBandWidth': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
