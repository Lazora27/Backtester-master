import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerBandWidth_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerBandWidth und MassIndex
    """
    
    params = (
        ('indicators', {
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'KeltnerBandWidth': 1.0,
            'MassIndex': 1.0
        })
    )
