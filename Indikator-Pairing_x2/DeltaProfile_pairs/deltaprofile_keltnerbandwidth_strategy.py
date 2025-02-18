import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
