import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerBandWidth_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerBandWidth und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'KeltnerBandWidth': 1.0,
            'ModifiedATR': 1.0
        })
    )
