import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerBandWidth_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerBandWidth und DemandIndex
    """
    
    params = (
        ('indicators', {
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'KeltnerBandWidth': 1.0,
            'DemandIndex': 1.0
        })
    )
