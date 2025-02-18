import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_RateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und RateOfChange
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'RateOfChange': 1.0
        })
    )
